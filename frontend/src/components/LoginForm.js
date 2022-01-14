import React, { useEffect, useState } from "react";
import Cookies from "universal-cookie";
import '../App.css';

const LoginForm = () => {

  const cookies = new Cookies();

  const login = () => {
    const url = "http://localhost:8000/api/pet/";

    fetch("/api/login/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": cookies.get("csrftoken"),
        },
        credentials: "same-origin",
        body: JSON.stringify({email: 'shelter@mail.com', password: 'password'}),
      })
      .then(this.isResponseOk)
      .then((data) => {
        console.log(data);
        this.setState({isAuthenticated: true, username: "", password: "", error: ""});
      })
      .catch((err) => {
        console.log(err);
        this.setState({error: "Wrong username or password."});
      });
  }

  login()

  return (
    <div className='login'>

    </div>
  )
};

export default LoginForm;