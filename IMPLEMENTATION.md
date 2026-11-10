# Cloud9 compatibility patch

Upstream:
https://github.com/hhftechnology/pangolin-cloudflare-tunnel

Upstream commit:
593713055da906f5ef010e968068e8e85858dc17

Local changes:
1. Traefik TLS domains accepts current structured API format.
2. Cloudflare origin NoTLSVerify=false.
3. CLOUDFLARE_API_TOKEN_FILE support.
4. Latest Go builder.
5. Stripped Go binary.
6. Runtime UID/GID 65532:65532.

Reason:
Upstream latest currently expects tls.domains as []string while
current Traefik exposes structured Domain objects.
