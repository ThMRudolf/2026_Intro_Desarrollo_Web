export function SingleTask({
  id,
  texto,
  colorFondo,
  estaCompletada,
  completarTarea,
}) {
  return (
    <div className="task">
      <input
        type="checkbox"
        checked={estaCompletada}
        onChange={() => completarTarea(id)}
      />

      <span
        className={estaCompletada ? "task-text completed" : "task-text"}
        style={{ backgroundColor: colorFondo }}
      >
        {texto}
      </span>
    </div>
  );
}