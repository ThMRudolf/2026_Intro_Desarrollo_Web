import CarrerasConParametros from "./Carreras";

function Programas() {
    return(
        <div>
            <h1>Programas</h1>
            <CarrerasConParametros/>
            <CarrerasConParametros/>

        </div>
    );
}

export function ProgramasConArreglo() {
    const carreras = [
        {
            url: "https://carreras.itam.mx/wp-content/uploads/2025/07/mini-2025-industrial.webp",
            nombre: "Ingeniería Industrial y Sistemas Inteligentes",
            plan_de_estudios: "https://industrial.itam.mx/es/plan-de-estudios/"
        },
        {
            url: "https://carreras.itam.mx/wp-content/uploads/2025/07/mini-2025-mecatronica.webp",
            nombre: "Ingeniería en Mecatronica y Robotica Inteligente",
            plan_de_estudios: "https://mecatronica.itam.mx/es/plan-de-estudios/"
        },
        {
            url: "https://carreras.itam.mx/wp-content/uploads/2025/07/mini-2025-negocios.webp",
            nombre: "Ingeniería en Negocios",
            plan_de_estudios: "https://ingnegocios.itam.mx/plan-de-estudios/"
            
        },
        {
            url: "https://carreras.itam.mx/wp-content/uploads/2025/07/mini-2025-compu.webp",
            nombre: "Ingeniería y Ciencias en Computación",
            plan_de_estudios: "https://ingnegocios.itam.mx/plan-de-estudios/"
        }
    ];
    return (
        <div>
            <h1>Programas del ITAM</h1>
            {carreras.map((carrera, index) => (
                <CarrerasConParametros
                    key={index}
                    url={carrera.url}
                    nombre={carrera.nombre}
                    plan_de_estudios={carrera.plan_de_estudios}
                />
            ))}
        </div>
    );
}
