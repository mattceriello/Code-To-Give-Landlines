import React, { useState } from "react";
import { useNavigate } from "react-router";
import { useDispatch } from "react-redux";
import Profile from "../components/Profile";
import { setCredentials } from "../features/user/user";
import registerImg from "../assets/register.svg";
import "../styles/Login.css";
import { Link } from "react-router-dom";
import { useRegisterMutation } from "../services/userApi";
const Register = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [register, { isLoading }] = useRegisterMutation();
  const [inputs, setInputs] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  console.log(inputs);
  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      const user = await register(inputs).unwrap();
      dispatch(setCredentials(user));
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="login">
      <div className="register-left">
        <div className="left-wrapper">
          <p>We empower those experiencing homelessness in Atlanta</p>
          <img src={registerImg} />
        </div>
      </div>
      <div className="register-right">
        <form className="register-form" onSubmit={handleSubmit}>
          <h1>Register</h1>
          <div className="register-inputs">
            <div className="register-input">
              <label htmlFor="firstName"> First name </label>
              <input
                placeholder="Enter your first name"
                name="firstName"
                value={inputs.firstName}
                onChange={handleChange}
              />
            </div>
            <div className="register-input">
              <label htmlFor="lastName">Last name</label>
              <input
                placeholder="Enter your last name"
                name="lastName"
                value={inputs.lastName}
                onChange={handleChange}
              />
            </div>
            <div className="register-input">
              <label htmlFor="email"> Email address </label>
              <input
                placeholder="Enter your email address"
                name="email"
                value={inputs.email}
                onChange={handleChange}
              />
            </div>
            <div className="register-input">
              <label htmlFor="password">Password</label>
              <input
                placeholder="Enter your password"
                name="password"
                value={inputs.password}
                onChange={handleChange}
              />
            </div>
            <div className="register-input">
              <label htmlFor="confirmPassword">Confirm password</label>
              <input
                placeholder="Confirm password"
                name="confirmPassword"
                value={inputs.confirmPassword}
                onChange={handleChange}
              />
            </div>
          </div>
          <p className="dontHaveAccount">
            Already have an account? <Link to="/login">Login </Link>
          </p>
          <button>Register</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
