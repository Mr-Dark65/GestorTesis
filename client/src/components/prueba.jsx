import React from 'react';
import { FaUserCircle, FaHome, FaSearch, FaPlus } from 'react-icons/fa'; // Importamos el icono de usuario, casa, lupa y más
import './prueba.css'; // Importamos el archivo CSS

export const Prueba = () => {
  const userName = localStorage.getItem('userName')
  return (
    <div className="main-container">
      <div className="header">
      <nav>
        <a href="/" className="nav-link">
          <div className="nav-bar">
            <FaHome className="home-icon" />
            <span className="home-text">Inicio</span>
          </div>
        </a>
      </nav>
      </div>
      <div className="container">
        <div className="header-content">
          <div className="icon-container">
            <FaUserCircle className="icon" />
          </div>
          <div className="username-container">
            <label htmlFor="username" className="username">{userName}</label>
          </div>
          <div className="filter-container">
            <select className="filter-combobox">
              <option value="">Filtro</option>
              {/* Añadir opciones de filtro. . . */}
            </select>
            <div>
    
    </div>
          </div>
          <div className="search-container">
            <input className="search-input" type="text" placeholder="Buscar" />
            <FaSearch className="search-icon" />
          </div>
          <button className="search-button">Filtrar</button>
        </div>
        <div className="add-student-container">
          <button className="add-student-button">
            <FaPlus className="plus-icon" />
          </button>
          <span className="add-student-text">Añadir Estudiante</span>
        </div>
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th className="wide-column">Estudiante</th>
                <th>Tema de tesis</th>
                <th>Progreso</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td></td>
                <td></td>
                <td></td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
              </tr>
            </tbody>
          </table>
          <button className="order-button">Ordenar</button>
        </div>
       </div>
    </div>
  );
}

