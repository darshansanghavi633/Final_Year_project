import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import axios from "axios";
import TextToImage from "./TextToImage";
import { Container, Spinner, Card, Image, Row } from "react-bootstrap";

const AuthCallback: React.FC = () => {
  const [searchParams] = useSearchParams();
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    const code = searchParams.get("code");
    if (code) {
      axios
        .get(`http://localhost:5000/auth/linkedin/callback?code=${code}`)
        .then((res) => setUser(res.data))
        .catch(console.error);
    }
  }, [searchParams]);

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        {user && user.profile ? (
          <Card
            className="p-4 shadow-lg text-center w-100"
            style={{ maxWidth: "500px" }}
          >
            <Card.Body>
              <h4 className="mb-3 text-primary" style={{ fontSize: "1.5rem" }}>
                Welcome, {user.profile.name}
              </h4>
              <p className="text-muted mb-3" style={{ fontSize: "1rem" }}>
                Email: {user.profile.email || "No email available"}
              </p>
              {user.profile.picture ? (
                <Image
                  src={user.profile.picture}
                  alt="Profile"
                  roundedCircle
                  width={120}
                  height={120}
                  className="mb-3 shadow-lg"
                  style={{ border: "2px solid #ddd" }}
                />
              ) : (
                <p>No Profile Picture</p>
              )}
            </Card.Body>
          </Card>
        ) : (
          <div className="text-center">
            <Spinner animation="border" size="sm" />
            <p className="mt-2 text-muted">Loading your profile...</p>
          </div>
        )}
        <div className="mt-5 w-100">
          <TextToImage />
        </div>
      </Row>
    </Container>
  );
};

export default AuthCallback;
