import  RoleForm  from "../components/roleform"
import { useNavigate } from 'react-router-dom';
export function RoleFormPage(){

    const navigate = useNavigate();
    const save = (data) => {
        const saveData = async (data) => {
            
            const permissions = await fetch ("http://127.0.0.1:8000/permissions/")
            const permissionsIds = await permissions.json()
            const permissionId = permissionsIds.findIndex(permiso=>permiso.name===data.permission)
            data.permission=[permissionId+1]
            console.log(data.permission)
            const save = await fetch('http://127.0.0.1:8000/roles/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            const response = await save.json()
            console.log(response)
            if(response.active){
                navigate("/")
            }
        }
        saveData(data)
    }

    return(
        <div className="role-list-page">
            <header className="header">
                <h1>Crear Rol</h1>
                
            </header>
            <main className="main">
                <RoleForm onsubmit={save}/>
            </main>
        </div>
    )
}
