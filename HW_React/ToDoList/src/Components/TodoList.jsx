import { useState } from "react";
import { SingleTask } from "./SingleTask";
import "./TodoList.css";

export function TodoList() {
  const [tareas, setTareas] = useState([
    {
      id: 1,
      texto: "Clean my room",
      colorFondo: "#d88a00",
      estaCompletada: false,
    },
    {
      id: 2,
      texto: "Decluttering my study room",
      colorFondo: "#f2b13c",
      estaCompletada: false,
    },
    {
      id: 3,
      texto: "Buy some new stationary",
      colorFondo: "#f5a000",
      estaCompletada: false,
    },
    {
      id: 4,
      texto: "Spa pedicure and manicure",
      colorFondo: "#f6bc52",
      estaCompletada: false,
    },
    {
      id: 5,
      texto: "Playing basketball with friends",
      colorFondo: "#d99a2b",
      estaCompletada: false,
    },
    {
      id: 6,
      texto: "Reduce fast food",
      colorFondo: "#d6a454",
      estaCompletada: false,
    },
  ]);

  function completarTarea(id) {
    const nuevasTareas = tareas.map((tarea) => {
      if (tarea.id === id) {
        return {
          ...tarea,
          estaCompletada: !tarea.estaCompletada,
        };
      }

      return tarea;
    });

    setTareas(nuevasTareas);
  }

  return (
    <div className="todo-container">
      <h1>To Do List</h1>

      {tareas.map((tarea) => (
        <SingleTask
          key={tarea.id}
          id={tarea.id}
          texto={tarea.texto}
          colorFondo={tarea.colorFondo}
          estaCompletada={tarea.estaCompletada}
          completarTarea={completarTarea}
        />
      ))}
    </div>
  );
}