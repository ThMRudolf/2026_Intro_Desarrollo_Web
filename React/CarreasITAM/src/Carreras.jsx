const CarrerasConParametros= ({url, nombre, plan_de_estudios}) => {
    return(
        <div>
            <h2>{nombre}</h2>
            <img 
                src={url} 
                alt={nombre}
            />
            <p><a href={plan_de_estudios} target="_blank" rel="noopener noreferrer">Plan de Estudios</a></p>
        </div>
    );
}
export default CarrerasConParametros; 