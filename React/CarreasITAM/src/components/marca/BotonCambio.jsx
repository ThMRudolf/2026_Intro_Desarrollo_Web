export function BotonCambio({ operacion, cambiar, numero }) {
    operacion === "sumar" ? cambiar(prev => prev + numero) : cambiar(prev => prev );
    operacion === "multiplicar" ? cambiar(prev => prev * numero) : cambiar(prev => prev);
    operacion === "restar" ? cambiar(prev => prev - numero) : cambiar(prev => prev);
}

return (
    <div>
        <BotonCambio operacion="sumar" cambiar={setContador} numero={1} />  
        <BotonCambio operacion="multiplicar" cambiar={setContador} numero={2} />
        <BotonCambio operacion="restar" cambiar={setContador} numero={1} />
    </div>
);