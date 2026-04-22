const CarrerasConParametros= ({url, nombre}) => {
    return(
        <div>
            <h2>{nombre}</h2>
            <img 
                src={url} 
                alt={nombre}
            />
        </div>
    );
}
export default CarrerasConParametros; 