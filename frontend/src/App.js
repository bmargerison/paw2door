import React, { Component } from "react";
import "./App.css";
import Cookies from "universal-cookie";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import SignUp from "./components/pages/SignUp";
import Login from "./components/pages/Login";
import Pets from "./components/pages/Pets";
import Shelter from "./components/pages/Shelter";

const cookies = new Cookies();

class App extends Component {
  render() {
    return (
      <>
        <Router>
          <Routes>
            <Route path="/" element={<Pets />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/login" element={<Login />} />
            <Route path="/shelter/:id" element={<Shelter />} />
          </Routes>
        </Router>
      </>
    );
  }
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      error: "",
      isAuthenticated: false,
    };
  }

  componentDidMount = () => {
    this.getSession();
  };

  getSession = () => {
    fetch("/api/session/", {
      credentials: "same-origin",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.isAuthenticated) {
          this.setState({ isAuthenticated: true });
        } else {
          this.setState({ isAuthenticated: false });
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  whoami = () => {
    fetch("/api/whoami/", {
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "same-origin",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("You are logged in as: " + data.email);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  handlePasswordChange = (event) => {
    this.setState({ password: event.target.value });
  };

  handleEmailChange = (event) => {
    this.setState({ email: event.target.value });
  };

  isResponseOk(response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  login = (event) => {
    event.preventDefault();
    fetch("/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get("csrftoken"),
      },
      credentials: "same-origin",
      body: JSON.stringify({
        email: this.state.email,
        password: this.state.password,
      }),
    })
      .then(this.isResponseOk)
      .then((data) => {
        console.log(data);
        this.setState({
          isAuthenticated: true,
          email: "",
          password: "",
          error: "",
        });
      })
      .catch((err) => {
        console.log(err);
        this.setState({ error: "Wrong email or password." });
      });
  };

  logout = () => {
    fetch("/api/logout", {
      credentials: "same-origin",
    })
      .then(this.isResponseOk)
      .then((data) => {
        console.log(data);
        this.setState({ isAuthenticated: false });
      })
      .catch((err) => {
        console.log(err);
      });
  };

  render() {
    if (!this.state.isAuthenticated) {
      return (
        <div className="container mt-3">
          <h1>React Cookie Auth</h1>
          <br />
          <h2>Login</h2>
          <form onSubmit={this.login}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="text"
                className="form-control"
                id="email"
                name="email"
                value={this.state.email}
                onChange={this.handleEmailChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Password</label>
              <input
                type="password"
                className="form-control"
                id="password"
                name="password"
                value={this.state.password}
                onChange={this.handlePasswordChange}
              />
              <div>
                {this.state.error && (
                  <small className="text-danger">{this.state.error}</small>
                )}
              </div>
            </div>
            <button type="submit" className="btn btn-primary">
              Login
            </button>
          </form>
        </div>
      );
    }
    return (
      <div className="container mt-3">
        <h1>React Cookie Auth</h1>
        <p>You are logged in!</p>
        <button className="btn btn-primary mr-2" onClick={this.whoami}>
          WhoAmI
        </button>
        <button className="btn btn-danger" onClick={this.logout}>
          Log out
        </button>
      </div>
    );
  }
}

export default App;
