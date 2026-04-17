const getUserData = async () => {
	console.log("Requesting data...");
	const response = await fetch(`https://api.restful-api.dev/objects`);
	console.log("Data retrieved!");
	return response.json();
}

const data = await getUserData();
// console.log(data);

for (const item of data) {
    if (item.data != null) {

        let details = "";

        for (const key in item.data) {
            details += `${key}: ${item.data[key]}, `;
        }
        details = details.slice(0, -2);

        const objectAPI = `${item.name} (${details})`;
        console.log(objectAPI)
    }
}