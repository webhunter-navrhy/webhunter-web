import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';

Deno.serve(async (req) => {
  try {
    const base44 = createClientFromRequest(req);

    const { name, company, email, phone, message } = await req.json();

    // Save to database (service role so it persists regardless of user)
    try {
      await base44.asServiceRole.entities.LeadInquiry.create({
        name,
        company: company || '',
        email,
        phone: phone || '',
        message: message || '',
        status: 'new'
      });
    } catch (dbErr) {
      console.error('DB save failed:', dbErr.message);
    }

    const resendApiKey = Deno.env.get("RESEND_API_KEY");
    if (!resendApiKey) return Response.json({ success: true, db: 'only' });

    const emailContent = `
Nová poptávka z kontaktního formuláře:

Jméno: ${name}
Firma: ${company || '—'}
Email: ${email}
Telefon: ${phone || '—'}

Zpráva:
${message || '—'}
    `.trim();

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${resendApiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'noreply@webhunter.cz',
        to: 'weboviny@email.cz',
        subject: `Nová poptávka od ${name}`,
        text: emailContent,
      }),
    });

    if (!response.ok) {
      const error = await response.text();
      return Response.json({ error: `Resend error: ${error}` }, { status: 500 });
    }

    return Response.json({ success: true });
  } catch (error) {
    return Response.json({ error: error.message }, { status: 500 });
  }
});