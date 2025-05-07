import React from "react";
import { Button, Container, Row, Col, Card } from "react-bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";

const LoginButton: React.FC = () => {
  const handleLogin = () => {
    window.location.href = "http://localhost:5000/auth/linkedin";
  };

  return (
    <Container
      fluid
      className="d-flex justify-content-center align-items-center min-vh-100 bg-gradient bg-light"
    >
      <Row className="w-100 justify-content-center">
        <Col md={6} lg={4}>
          <Card className="shadow-lg border-0 rounded-4 p-4 text-center">
            <Card.Body>
              <Card.Title className="mb-4 fs-3 fw-bold text-primary">
                Welcome to AI Image Generator
              </Card.Title>
              <Button
                variant="primary"
                size="lg"
                onClick={handleLogin}
                className="rounded-pill px-4 py-2 d-flex align-items-center justify-content-center gap-2"
              >
                <i className="bi bi-linkedin fs-5"></i>
                Sign in with LinkedIn
              </Button>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default LoginButton;
