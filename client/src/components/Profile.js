import React from "react";
import { useSelector } from "react-redux";
const Profile = () => {
  //Testing to see if user info is stored
  const user = useSelector((state) => state.user.value);
  return (
    <div>
      <h1>Profile</h1>
      <p>name {user.name}</p>
      <p>age {user.age}</p>
      <p>Email {user.email}</p>
    </div>
  );
};

export default Profile;
