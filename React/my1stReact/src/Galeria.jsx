const Perfil= ({url, nombre}) =>{
    return(
        <div>
            <img 
                src={url} 
                alt={nombre}
            />
        </div>
    );
}

export default function Galeria() {
    return(
        <div>
            <h1>Galeria</h1>
            <Perfil url={
                "https://tse2.mm.bing.net/th/id/OIP.Os5J_8G065AgsEGSST3NVgHaE8?pid=Api&P=0&h=180"
                }
                 nombre={"Colmillo"} 
                />
            <Perfil url={
                "https://tse3.mm.bing.net/th/id/OIP.AGcs3wiT68bSFnP_92NvuQHaI4?pid=Api&P=0&h=180"
                }
                nombre={"Fahra"}
                />
    
        </div>
    );
}
