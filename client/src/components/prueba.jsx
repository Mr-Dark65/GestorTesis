import React, { useState, useEffect } from "react";
import { FaHome, FaUserCircle, FaSearch, FaPlus } from "react-icons/fa";
import axios from "axios"; // Importamos axios para hacer solicitudes HTTP
import "./prueba.css"; // Importamos el archivo CSS

export const Prueba = () => {
  const userName = localStorage.getItem("userName");
  const userId = localStorage.getItem("userId"); // Obtener el ID del tutor actual

  const [selectedFilter, setSelectedFilter] = useState("estudiantes"); // Opción para la búsqueda
  const [estudiantes, setEstudiantes] = useState([]); // Estado para almacenar los estudiantes

  const handleFilterChange = (event) => {
    setSelectedFilter(event.target.value);
    setSearchInput("");
  };

  useEffect(() => {
    // Función para obtener los estudiantes asociados al tutor actual
    const fetchEstudiantes = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/project/api/filter-options/");
        const estudiantesData = response.data.estudiantes;
        // Filtrar los estudiantes asociados al tutor actual (según el ID)
        const filteredEstudiantes = estudiantesData.filter(estudiante => estudiante.id_tutor_pertenece === parseInt(userId));
        setEstudiantes(filteredEstudiantes);
      } catch (error) {
        console.error("Error al obtener estudiantes:", error);
      }
    };

    fetchEstudiantes(); // Llamar a la función para obtener los estudiantes
  }, [userId]); // Llamar useEffect cada vez que cambia el userId

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
            <label htmlFor="username" className="username">
              {userName}
            </label>
          </div>
          <div className="filter-container">
            <select
              className="filter-combobox"
              value={selectedFilter}
              onChange={handleFilterChange}
            >
              <option value="estudiantes">Estudiantes</option>
              <option value="carreras">Carreras</option>
              <option value="avance">Avance</option>
            </select>
            <div></div>
          </div>
          <div className="search-container">
            <input
              className="search-input"
              type="text"
              placeholder="Buscar"
            />
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
              {/* Mapear los estudiantes y renderizar cada fila */}
              {estudiantes.map(estudiante => (
                <tr key={estudiante.id_estudiante}>
                  <td>{estudiante.nombre} {estudiante.apellido}</td>
                  <td>{estudiante.tema_tesis}</td>
                  <td>{/* Colocar el progreso del estudiante */}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button className="order-button">Ordenar</button>
        </div>
      </div>
    </div>
  );
};
