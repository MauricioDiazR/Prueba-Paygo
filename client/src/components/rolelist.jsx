
export default function RoleList({roles}){
    return(
        <ul>
            {roles.map(role => (
                <li className="role-name" key={role.id}>{role.name} - <a href={`/roles-edit/${role.id}`}>Editar</a></li>
            ))}
        </ul>
    )
}