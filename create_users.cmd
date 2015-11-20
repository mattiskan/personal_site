use admin;
db.createUser({
    user: "system",
    pwd: "password",
    roles: [{
        role: "root",
        db: "admin"
    }, {
        role: "restore",
        db: "admin"
    }
           ]
});

use testlol;
db.createUser({
    user: "django",
    pwd: "a453d01f76d6d6c32de8c7e11243867d05ff7138",
    "roles": [
        {
            "role": "readWrite",
            "db": "testlol"
        }
    ]
});
