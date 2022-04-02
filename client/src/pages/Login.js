import React from "react";
import { useDispatch } from "react-redux";
import Profile from "../components/Profile";
import { login, logout } from "../features/user/user";
import loginImg from "../assets/login.svg";
import blackWave from "../assets/blackwave.svg";
import "../styles/Register.css";
import { Link } from "react-router-dom";
const Login = () => {
  const dispatch = useDispatch();
  return (
    <div className="register">
      <div className="register-left">
        <div className="left-wrapper">
          <p>
            We transform, through Christ, the lives of those facing
            homelessness.
          </p>
          <img src={loginImg} />
        </div>
      </div>
      <div className="login-right">
        <form className="login-form">
          <h1>Login</h1>
          <div className="login-inputs">
            <div className="login-input">
              <label htmlFor="email"> Email address </label>
              <input placeholder="Enter your email address" />
            </div>
            <div className="login-input">
              <label htmlFor="password">Password</label>
              <input placeholder="Enter your password" />
            </div>
          </div>
          <p className="haveAccount">
            Don't have an account? <Link to="/register">Register </Link>
          </p>
          <button>Login</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
