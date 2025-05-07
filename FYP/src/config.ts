interface LinkedInApiConfig {
  clientId: string;
  redirectUrl: string;
  oauthUrl: string;
  scope: string;
  state: string;
}

export const LinkedInApi: LinkedInApiConfig = {
  clientId: "77dgfwxt6egxpn",
  redirectUrl: "http://localhost:5173/auth/linkedin/callback",
  oauthUrl: "https://www.linkedin.com/oauth/v2/authorization",
  scope: "r_liteprofile r_emailaddress",
  state: "129856", // Change this for security
};
