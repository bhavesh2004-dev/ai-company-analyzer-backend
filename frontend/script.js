async function analyzeCompany() {
    const url = document.getElementById("urlInput").value;
    const loading = document.getElementById("loading");
    const companyCard = document.getElementById("companyCard");
    const proposalCard = document.getElementById("proposalCard");

    if (!url) {
        alert("Please enter a URL");
        return;
    }

    companyCard.classList.add("hidden");
    proposalCard.classList.add("hidden");
    loading.classList.remove("hidden");

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/analyze?url=${encodeURIComponent(url)}`,
            { method: "POST" }
        );

        const result = await response.json();
        loading.classList.add("hidden");

        const data = result.data;

        // ---------- COMPANY CARD ----------
        const company = data.company_profile;

        companyCard.innerHTML = `
            <h2>🏢 Company Overview</h2>

            <div class="section">
                <strong>Company Name:</strong> ${company.company_name}
            </div>

            <div class="section">
                <strong>About:</strong>
                <p>${company.about_company}</p>
            </div>

            <div class="section">
                <strong>Services:</strong>
                <ul>${company.services.map(s => `<li>${s}</li>`).join("")}</ul>
            </div>

            <div class="section">
                <strong>Technologies:</strong>
                <ul>${company.technologies.map(t => `<li>${t}</li>`).join("")}</ul>
            </div>

            <div class="section">
                <strong>Team:</strong>
                <p>${company.team_or_employees}</p>
            </div>
        `;

        // ---------- PROPOSAL CARD ----------
        const proposal = data.proposal;

        proposalCard.innerHTML = `
            <h2>📧 Outreach Proposal</h2>

            <div class="section">
                <strong>Subject:</strong>
                <p>${proposal.subject}</p>
            </div>

            <div class="email-box">
                ${proposal.email_body}
            </div>
        `;

        companyCard.classList.remove("hidden");
        proposalCard.classList.remove("hidden");

    } catch (error) {
        loading.classList.add("hidden");
        alert("Error occurred. Check console.");
        console.error(error);
    }
}
