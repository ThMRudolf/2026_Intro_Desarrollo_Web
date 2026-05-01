export function BotonMarca({ texto, tipo }) {
/*
    let colorConIf = "";
    if (tipo === "primary") {
    colorConIf = "purple";
    } else {
        colorConIf = "white";
    }
*/
const colorFondo = tipo === "primary" ? "purple" : "white";
const colorTexto = tipo === "primary" ? "white" : "black";

    return (
        <button style={{ backgroundColor: colorFondo, color: colorTexto }}>
            {texto}
        </button>
    );
}