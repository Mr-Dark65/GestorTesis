import React, { useState } from 'react';
import axios from 'axios';
import {toast} from 'react-hot-toast'
import './LoginForm.css';

export const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/project/api/users/');

      const user = response.data.find(user => user.correo === email && user.password === password);

      if (user) {
        localStorage.setItem('userName', user.tutor.nombre);
        localStorage.setItem('userId', user.id_usuario);
        window.location.href = '/Prueba';
        setError('');
      } else {
        toast.error("Correo o Contraseña incorrectos", {
          position: "top-left",
          style: {
            marginTop: '5rem',
          }
        })
      }
    } catch (error) {
      console.error('Error al iniciar sesión:', error);
      setError('Error al iniciar sesión. Por favor, inténtalo de nuevo más tarde.');
    }
  };

  return (
    <div className='content-box'>
      <div className="imagen">
        <img src="/images/logo-sitio-fisei-2020.png" alt="logo-fisei" />
      </div>
      <h2>Iniciar Sesión</h2>
      <div className='content-input'>
        <label htmlFor="email">Correo:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className='content-input'>
        <label htmlFor="password">Contraseña:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button className='button-inicio' onClick={handleLogin}>Iniciar Sesión</button>
      {error && <p>{error}</p>}
    </div>
  );
};

