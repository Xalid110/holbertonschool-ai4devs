
function fetchUser(userId) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                id: userId,
                name: "Alex",
                active: true
            });
        }, 500);
    });
}

async function getUserName(userId) {
    const user = fetchUser(userId);
    return user.name;
}

async function main() {
    const name = await getUserName(1);
    console.log("User name:", name);
}

main();
