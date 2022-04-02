import React from "react";
import Login from "./pages/Login";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import "./App.css";
import Register from "./pages/Register";
import Profile from "./components/Profile";

function App() {
  return (
    <BrowserRouter basename="/">
      <div className="App">
        <Routes>
          <Route path="/" element={<Profile />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
