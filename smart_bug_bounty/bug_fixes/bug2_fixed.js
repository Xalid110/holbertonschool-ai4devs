
function fetchUser(userId) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                id: userId,
                name: "Alex",
                active: true
            });
        }, 100);
    });
}

async function getUserName(userId) {
    const user = await fetchUser(userId);
    return user.name;
}

async function main() {
    console.assert(await getUserName(1) === "Alex");
    console.assert(await getUserName(2) === "Alex");
    console.log("All bug2 tests passed!");
}

main();
