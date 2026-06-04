import { useState } from "react";


function LoginForm({ onLogin }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    async function handleSubmit(event) {
        event.preventDefault();

        const response = await fetch("http://127.0.0.1:8000/auth/login", {
            method: "POST",
            body: new URLSearchParams({
                username: email,
                password,
            }),
        });

        if (!response.ok) {
            console.log("Login failed");
            return;
        }

        const token = await response.json();

        localStorage.setItem("accessToken", token.access_token);
        onLogin(token.access_token);
    }

    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="email"
                placeholder="Email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
            />

            <button type="submit">Login</button>
        </form>
    );
}

export default LoginForm;