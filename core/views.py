from django.shortcuts import render

def landing_view(request):
    faq_list = [
        ("Do customers need an account?", "No—feedback is anonymous and requires only a QR scan."),
        ("How many branches can I add?", "1 branch on free tier, paid plans coming soon."),
        ("Can I export the data?", "Yes—CSV export is available per branch or site-wide."),
        ("Is there a free tier?", "Yes—1 branch and 20 responses/month free; paid plans coming soon.")
    ]
    return render(request, "landing.html", {"faq_list": faq_list})