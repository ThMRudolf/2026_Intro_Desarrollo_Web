import {useState} from 'react';


const PantallaConBotonConEstado = () => {
    const [count, setCount] = useState(0);

    return (
        <div>
            <h1>Contador: {count}</h1>
            <h2>Sum +10</h2>
            <button onClick={() => setCount(count + 10)}>
                Incrementar
            </button>
            
            <h2>Minus +5: </h2>
            <button onClick={() => setCount(count - 5)}>
                Decrementar
            </button>
            
            <h2>Mulitply -1: </h2>
            <button onClick={() => setCount(count *(-1))}>
                cambiar signo
            </button>
            
            <h2>Minus -2: </h2>
            <button onClick={() => setCount(count - 2)}>
                Decrementar
            </button>
            
            <h2>Sum +1:</h2>
            <button onClick={() => setCount(count + 1)}>
                Incrementar
            </button>
        </div>
    );
};

export default PantallaConBotonConEstado;