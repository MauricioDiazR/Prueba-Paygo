import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import  RoleForm  from "../components/roleform"
import { useNavigate } from 'react-router-dom';

export default function RoleEditPage(props){
    const [role, setRole] = useState({})
    const { id } = useParams();
    const navigate = useNavigate();
    useEffect(() => {
        const getRole = async () => {
            const response = await fetch(`http://127.0.0.1:8000/roles/${id}/`)
            const data = await response.json()
            const permiso = await fetch(`http://127.0.0.1:8000/permissions/${data.permission[0]}/`)
            const permisoData = await permiso.json()
            data.permission = [permisoData.name]
            setRole(data)
        }
        getRole()
    }, [id])

    const edit = (data) => {
        const update = async (data) => {
            const permissions = await fetch ("http://127.0.0.1:8000/permissions/")
            const permissionsIds = await permissions.json()
            const permissionId = permissionsIds.findIndex(permiso=>permiso.name===data.permission)
            data.permission=[permissionId+1]
            const save = await fetch(`http://127.0.0.1:8000/roles/${id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            const response = await save.json()
            if(response.active){
                navigate("/")
            }
        }
        update(data)
    }

    return(
        <div className="role-list-page">
            <header className="header">
                <h1>Editar Rol: {id} - {role?.name}</h1>
                
            </header>
            <main className="main">
                <RoleForm onsubmit={edit}  role={role}/>
            </main>
        </div>
    )
}