from flask import Flask

app = Flask(__name__)

RESUME_HTML = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Sumit Amitkumar Soni - Resume</title>
    <link href='https://fonts.googleapis.com/css?family=Montserrat:700,400|Roboto:400,300'
        rel='stylesheet'>
    <link rel='stylesheet'
        href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'>
    <style>
        body {
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
            font-family: 'Roboto', Arial, sans-serif;
            color: #222;
            margin: 0;
            padding: 0;
        }
        .resume-container {
            max-width: 900px;
            margin: 40px auto;
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 8px 32px rgba(44, 62, 80, 0.15);
            padding: 40px 48px;
        }
        .header {
            text-align: center;
            margin-bottom: 32px;
        }
        .header h1 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.8em;
            margin: 0;
            color: #2d3e50;
        }
        .header .contact {
            margin-top: 12px;
            font-size: 1.1em;
            color: #555;
        }
        .header .contact a {
            color: #0077b5;
            text-decoration: none;
            margin: 0 8px;
        }
        .section-title {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.3em;
            color: #0077b5;
            margin-top: 32px;
            margin-bottom: 12px;
            letter-spacing: 1px;
            border-bottom: 2px solid #e0eafc;
            display: inline-block;
            padding-bottom: 2px;
        }
        ul {
            padding-left: 20px;
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 18px;
            margin-bottom: 0;
        }
        .skills-list li {
            background: #e0eafc;
            border-radius: 8px;
            padding: 6px 16px;
            font-size: 1em;
            color: #2d3e50;
            margin-bottom: 8px;
            list-style: none;
        }
        .exp-role {
            font-weight: bold;
            color: #2d3e50;
        }
        .exp-company {
            color: #0077b5;
            font-weight: 500;
        }
        .exp-date {
            color: #888;
            font-size: 0.98em;
        }
        .achievements {
            margin-top: 8px;
        }
        .education {
            margin-bottom: 0;
        }
        .cert-list {
            margin-bottom: 0;
        }
        .projects-list {
            margin-bottom: 0;
        }
        @media (max-width: 600px) {
            .resume-container {
                padding: 18px 8px;
            }
        }
    </style>
</head>
<body>
    <div class='resume-container'>
        <div class='header'>
            <h1>Sumit Amitkumar Soni</h1>
            <div class='contact'>
                Navi Mumbai, Maharashtra &nbsp;|&nbsp;
                <a href='mailto:sumit.a.soni2001@gmail.com'>
                    <i class='fa fa-envelope'></i> sumit.a.soni2001@gmail.com
                </a> &nbsp;|&nbsp;
                <i class='fa fa-phone'></i> +91 8850070610 &nbsp;|&nbsp;
                <a href='https://www.linkedin.com/in/sumit-s-030717116' target='_blank'>
                    <i class='fab fa-linkedin'></i> LinkedIn
                </a>
            </div>
        </div>

        <div>
            <div class='section-title'>Professional Summary</div>
            <p>GCP Cloud Engineer with 4+ years of IT experience,
            transitioning from .NET development to cloud engineering.
            Skilled in Kubernetes, IAM, CI/CD (GitHub Actions, Git, Helm, ArgoCD),
            and cloud observability tools (Datadog, Splunk, PagerDuty, BigPanda).
            Hands-on expertise in infrastructure automation, monitoring,
            and client-facing collaboration.
            Certified Google Cloud Professional Cloud Architect
            and Microsoft Azure Fundamentals (AZ-900).
            Passionate about designing cloud-native solutions, system optimization,
            and enhancing platform reliability.</p>
        </div>

        <div>
            <div class='section-title'>Core Skills</div>
            <ul class='skills-list'>
                <li>Google Cloud Platform (GCP)</li>
                <li>Microsoft Azure</li>
                <li>Kubernetes</li>
                <li>Docker</li>
                <li>Git</li>
                <li>Helm</li>
                <li>ArgoCD</li>
                <li>GitHub Actions</li>
                <li>CI/CD</li>
                <li>Datadog</li>
                <li>Splunk</li>
                <li>PagerDuty</li>
                <li>BigPanda</li>
                <li>Python</li>
                <li>Shell</li>
                <li>Terraform</li>
                <li>YAML</li>
                <li>Jira</li>
                <li>Confluence</li>
                <li>GitHub Copilot</li>
                <li>SQL</li>
                <li>Agile</li>
                <li>Infrastructure as Code</li>
                <li>Site Reliability Engineering</li>
            </ul>
        </div>

        <div>
            <div class='section-title'>Professional Experience</div>
            <div class='exp-role'>Software Engineer</div>
            <span class='exp-company'>LTIMindtree</span>
            <span class='exp-date'>| Aug 2021 – Present | Navi Mumbai, Maharashtra</span>
            <ul>
                <li>Serve as GCP Cloud Engineer specializing in infrastructure automation, DevOps,
                observability and cloud-native solutions.</li>
                <li>Manage Kubernetes clusters on GCP: handling pods, logs, monitoring,
                    and enforcing IAM policies for secure access control.</li>
                <li>Build and maintain CI/CD pipelines using GitHub Actions, Helm, and ArgoCD,
                    improving deployment efficiency.</li>
                <li>Led incident management and system monitoring with Datadog, Splunk,
                PagerDuty, BigPanda, reducing downtime.</li>
                <li>Collaborated with cross-functional teams to optimize cloud operations
                    and resolve production issues quickly.</li>
            </ul>
            <div class='achievements'>
                <strong>Key Achievements:</strong>
                <ul>
                    <li>Built advanced Datadog monitors, dashboards, and synthetics
                        to improve performance visibility.</li>
                    <li>Designed Service Level Objectives (SLOs) and Event Logging Operations (ELOs)
                        to strengthen reliability.</li>
                    <li>Investigated and optimized SQL database performance,
                        integrating custom metrics.</li>
                    <li>Automated recurring reporting and monitoring tasks,
                        saving significant engineering hours.</li>
                </ul>
            </div>
        </div>

        <div>
            <div class='section-title'>Education</div>
            <ul class='education'>
                <li>Master of Technology (M.Tech) in Software Systems
                – BITS Pilani (Work Integrated Learning), 2021 – 2025</li>
                <li>Bachelor of Science (B.Sc.) in Information Technology
                – SIES College of Management Studies, 2018 – 2021<br>GPA: 9.00/10</li>
            </ul>
        </div>

        <div>
            <div class='section-title'>Certifications</div>
            <ul class='cert-list'>
                <li>Google Cloud Professional Cloud Architect – Google (Issued Sep 2025)</li>
                <li>Microsoft Certified: Azure Fundamentals (AZ-900)
                – Microsoft (Issued Feb 2022)</li>
                <li>Datadog 101: Developer – Datadog (Issued Jul 2023)</li>
                <li>Datadog Foundation – Datadog (Issued Jul 2023)</li>
                <li>Datadog Introduction to Observability – Datadog (Issued Jul 2023)</li>
                <li>GitHub Copilot Certifications (Microsoft, 2025):
                    <ul>
                        <li>Implement code improvements using GitHub Copilot tools</li>
                        <li>Develop code features using GitHub Copilot tools</li>
                        <li>Develop unit tests using GitHub Copilot tools</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div>
            <div class='section-title'>Projects</div>
            <ul class='projects-list'>
                <li><strong>CI/CD Automation on GCP</strong>
                – Designed GitHub Actions pipelines integrated with GCP Artifact Registry
                    and GKE,<br>
                    reducing release cycle times by 40%.</li>
                <li><strong>Cloud Monitoring Dashboards</strong>
                – Built Datadog dashboards and alerts to track real-time resource
                    utilization,<br>
                    enabling proactive scaling and cost savings.</li>
                <li><strong>Infrastructure Optimization</strong>
                – Automated Kubernetes resource scaling and IAM policy management,<br>
                    improving both security and cost efficiency.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def resume():
    html = (
        "<div>welcome to website deployed using a CI/CD pipeline.</div>" + RESUME_HTML
    )
    return Response(html, status=200, mimetype="text/html")


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
