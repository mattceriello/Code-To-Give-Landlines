import React, { useState } from "react";
import { useNavigate } from "react-router";
import { useDispatch } from "react-redux";
import Profile from "../components/Profile";
import { setCredentials } from "../features/user/user";
import loginImg from "../assets/login.svg";
import "../styles/Register.css";
import { Link } from "react-router-dom";
import { useLoginMutation } from "../services/userApi";
const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [login, { isLoading }] = useLoginMutation();
  const [inputs, setInputs] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      const user = await login(inputs).unwrap();
      dispatch(setCredentials(user));
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="login">
      <div className="login-left">
        <div className="left-wrapper">
          <p>
            We transform, through Christ, the lives of those facing
            homelessness.
          </p>
          <img src={loginImg} />
        </div>
      </div>
      <div className="login-right">
        <form className="login-form" onSubmit={handleSubmit}>
          <h1>Login</h1>
          <div className="login-inputs">
            <div className="login-input">
              <label htmlFor="email"> Email address </label>
              <input
                placeholder="Enter your email address"
                name="email"
                value={inputs.email}
                onChange={handleChange}
              />
            </div>
            <div className="login-input">
              <label htmlFor="password">Password</label>
              <input
                placeholder="Enter your password"
                name="password"
                value={inputs.password}
                onChange={handleChange}
              />
            </div>
          </div>
          <p className="haveAccount">
            Don't have an account? <Link to="/register">Register </Link>
          </p>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
