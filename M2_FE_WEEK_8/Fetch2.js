const createUser = async (name, mail, pass, address) => {

    const body = {
        name: name,
        data: {
            email: mail,
            password: pass,
            address: address,
        }
    };

    const response = await fetch("https://api.restful-api.dev/objects", {
        method: "POST",
        headers: {
            "x-api-key": "f2ee4a43-b231-4eea-991c-dc6661dd197c",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
    });

    const result = await response.json();
    console.log(result);
    return result;
};

createUser("Andres","cazuniga02@gmail.com","1234","Costa Rica");
