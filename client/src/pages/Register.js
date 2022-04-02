import React from "react";
import { useDispatch } from "react-redux";
import Profile from "../components/Profile";
import { login, logout } from "../features/user/user";
import registerImg from "../assets/register.svg";
import "../styles/Login.css";
import { Link } from "react-router-dom";
const Register = () => {
  const dispatch = useDispatch();
  return (
    <div className="login">
      <div className="register-left">
        <div className="left-wrapper">
          <p>We empower those experiencing homelessness in Atlanta</p>
          <img src={registerImg} />
        </div>
      </div>
      <div className="register-right">
        <form className="register-form">
          <h1>Register</h1>
          <div className="register-inputs">
            <div className="register-input">
              <label htmlFor="firstName"> First name </label>
              <input placeholder="Enter your first name" />
            </div>
            <div className="register-input">
              <label htmlFor="lastName">Last name</label>
              <input placeholder="Enter your last name" />
            </div>
            <div className="register-input">
              <label htmlFor="email"> Email address </label>
              <input placeholder="Enter your email address" />
            </div>
            <div className="register-input">
              <label htmlFor="password">Password</label>
              <input placeholder="Enter your password" />
            </div>
            <div className="register-input">
              <label htmlFor="confirmPassword">Confirm password</label>
              <input placeholder="Confirm password" />
            </div>
          </div>
          <p className="dontHaveAccount">
            Already have an account? <Link to="/login">Login </Link>
          </p>
          <button>Login</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
