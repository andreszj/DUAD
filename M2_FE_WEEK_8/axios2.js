import axios from 'axios';

const createUser = async (name, mail, pass, address) => {

    const body = {
        name: name,
        data: {
            email: mail,
            password: pass,
            address: address,
        }
    };

    const response = await axios.post("https://api.restful-api.dev/objects",body);

    const result = await response.data;
    console.log(result);
    return result;
};

createUser("Andres","cazuniga02@gmail.com","1234","Costa Rica");
