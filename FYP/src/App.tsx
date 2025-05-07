import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginButton from "./components/LoginButton";
import AuthCallback from "./components/AuthCallback";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from "react-bootstrap";

const App: React.FC = () => {
  return (
    <Router>
      <Container
        fluid
        className="min-vh-100 d-flex justify-content-center align-items-center bg-light"
      >
        <Routes>
          <Route path="/" element={<LoginButton />} />
          <Route path="/auth/linkedin/callback" element={<AuthCallback />} />
        </Routes>
      </Container>
    </Router>
  );
};

export default App;
