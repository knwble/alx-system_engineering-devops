# 0x10. HTTPS SSL
- Task 0: What is HTTPS ?
    1. A secure version of HTTP
    2. A faster version of HTTP
    3. A superior version of HTTP

- Task 1: Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

- Task 2: “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.

- Advanced Task 1: A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
