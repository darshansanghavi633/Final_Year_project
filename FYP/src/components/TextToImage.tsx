import React, { useState } from "react";
import { Container, Form, Button, Spinner, Card } from "react-bootstrap";

const TextToImage: React.FC = () => {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [image, setImage] = useState<string | null>(null);
  const [caption, setCaption] = useState<string | null>(null);
  const FASTAPI_URL = "https://b34c-34-105-94-205.ngrok-free.app/generate-image";
  const API_KEY = "wXXSZOOTVopWndju9tOcVBblW5B7s2K1Tt49DZBc7EA";

  const handleGenerate = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setImage(null);
    setCaption(null);

    try {
      // Step 1: Get caption from your backend
      const captionResponse = await fetch(
        "http://127.0.0.1:8000/generate-caption",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ topic: text }),
        }
      );

      let generatedCaption = "";
      if (captionResponse.ok) {
        const captionData = await captionResponse.json();
        generatedCaption = captionData.post;
        setCaption(generatedCaption);
      } else {
        console.error("Failed to fetch caption");
      }

      // Step 2: Call RapidAPI to generate the image (as binary)
      console.log(text)
      // await new Promise((resolve) => setTimeout(resolve, 15000));
      const imageResponse = await fetch(`${FASTAPI_URL}?prompt=${encodeURIComponent(text)}&api_key=${API_KEY}`, {
        method: "GET",
        mode: "cors",
        cache: "no-store",
      });
      


      if (!imageResponse.ok) {
        throw new Error("Image generation failed.");
      }
      console.log("Response content type:", imageResponse.headers.get('content-type'));

      
      window.open(`${FASTAPI_URL}?prompt=${encodeURIComponent(text)}&api_key=${API_KEY}`, '_blank');

    } catch (error) {
      console.error("Error generating image or caption:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="d-flex justify-content-center mt-5 w-100">
      <Card className="p-4 shadow-lg w-100" style={{ maxWidth: "600px" }}>
        <h3 className="mb-4 text-center text-primary">What's on your mind ?</h3>
        <Form>
          <Form.Group controlId="textInput">
            <Form.Control
              as="textarea"
              rows={3}
              className="mb-3"
              placeholder="Enter image description..."
              value={text}
              onChange={(e) => setText(e.target.value)}
              style={{
                resize: "none",
                borderRadius: "10px",
                boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
              }}
            />
          </Form.Group>
          <Button
            className="w-100 btn-primary py-2"
            onClick={handleGenerate}
            disabled={loading}
            style={{
              borderRadius: "8px",
              transition: "all 0.3s ease-in-out",
            }}
            onMouseOver={(e) =>
              (e.currentTarget.style.transform = "scale(1.05)")
            }
            onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1)")}
          >
            {loading ? (
              <>
                <Spinner animation="border" size="sm" /> Generating...
              </>
            ) : (
              "Generate Image"
            )}
          </Button>
        </Form>
        {loading && (
          <div className="mt-4 text-center">
            <Spinner animation="border" />
            <p className="mt-2 text-muted">Generating your image...</p>
          </div>
        )}
        {!loading && (
          <div className="mt-4 text-center">
            {caption && (
              <>
                <p className="fw-semibold mb-2">{caption}</p>
                <Button
                  variant="outline-primary"
                  className="mt-3 ms-2"
                  onClick={() => {
                    if (caption) navigator.clipboard.writeText(caption);
                  }}
                >
                  Copy Caption
                </Button>
              </>
            )}
            {/* <Card.Img
              variant="top"
              src={image}
              alt="Generated"
              className="rounded shadow-sm"
              style={{ maxWidth: "100%", height: "auto" }}
            /> */}

            {/* <Button
              variant="outline-success"
              className="mt-3"
              onClick={() => {
                const link = document.createElement("a");
                link.href = image;
                link.download = "generated-image.jpg";
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
              }}
            >
              Download Image
            </Button> */}
            <Button
              variant="outline-info"
              className="mt-3 ms-2"
              onClick={() => {
                const linkedInURL = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(
                  "https://yourwebsite.com" // Optional: Replace with your page URL
                )}&summary=${encodeURIComponent(caption || "")}`;
                window.open(linkedInURL, "_blank");
              }}
            >
              Post to LinkedIn
            </Button>
          </div>
        )}
      </Card>
    </Container>
  );
};

export default TextToImage;
