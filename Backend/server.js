// server.js
import express from 'express';
import axios from 'axios';
import cors from 'cors';
import dotenv from 'dotenv';
import fetch from 'node-fetch';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Load LinkedIn credentials from .env
const CLIENT_ID = process.env.LINKEDIN_CLIENT_ID;
const CLIENT_SECRET = process.env.LINKEDIN_CLIENT_SECRET;
const REDIRECT_URI = process.env.LINKEDIN_REDIRECT_URI;

console.log("Configured Redirect URI:", REDIRECT_URI);


// Step 1: Redirect to LinkedIn Authorization URL
app.get("/auth/linkedin", (req, res) => {
    const authUrl = `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(
        REDIRECT_URI
    )}&scope=${encodeURIComponent("openid profile email")}`;

    console.log("Generated Auth URL:", authUrl);
    res.redirect(authUrl);
});

// Step 2: Exchange authorization code for access token
app.get("/auth/linkedin/callback", async (req, res) => {
    const { code } = req.query;

    if (!code) {
        return res.status(400).json({ error: "Authorization code not found" });
    }

    try {
        const tokenResponse = await axios.post(
            "https://www.linkedin.com/oauth/v2/accessToken",
            new URLSearchParams({
                grant_type: "authorization_code",
                code,
                redirect_uri: REDIRECT_URI,
                client_id: CLIENT_ID,
                client_secret: CLIENT_SECRET,
            }),
            {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            }
        );

        const accessToken = tokenResponse.data.access_token;

        const userProfileResponse = await axios.get(
            "https://api.linkedin.com/v2/userinfo",
            {
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            }
        );

        res.json({
            profile: userProfileResponse.data,
        });
    } catch (error) {
        // console.error("LinkedIn OAuth error:", {
        //     message: error.message,
        //     status: error.response?.status,
        //     data: error.response?.data,
        // });
        // res.status(500).json({
        //     error: "Failed to authenticate",
        //     details: error.response?.data || error.message,
        // });
    }
});



app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
