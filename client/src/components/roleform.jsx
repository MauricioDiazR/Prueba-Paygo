import { useEffect, useState } from "react"

export default function RoleForm({onsubmit, role}){
    const [permisos, setPermisos] = useState([])
    const [defaultPermission, setDefaultPermission] = useState('')
    useEffect(()=>{
        const getPermissions = async () => {
            const permissions = await fetch ("http://127.0.0.1:8000/permissions/")
            const permissionsIds = await permissions.json()
            setPermisos(permissionsIds)
        }
        getPermissions()
    }, [])
    
    useEffect(() => {
         setDefaultPermission(role?.permission && role.permission.length > 0 ? role.permission[0] : '')
    },[role])

    const handleSubmit = (e) => {
        e.preventDefault()
        const data = Object.fromEntries(new FormData(e.target))
        onsubmit(data)
    }

    const handlePermissionChange = (e) => {
        const permission = e.target.value
        setDefaultPermission(permission)
    }

    return(
        <form className="form" onSubmit={handleSubmit}>
            <div className="input-control">
                <label>Nombre</label>
                <input type="text" name="name" defaultValue={role?.name} placeholder="Nombre del rol" required/>
            </div>
            <div className="input-control">
                <label>Permisos</label>
                <select name="permission"  value={defaultPermission} onChange={handlePermissionChange} required>
                    {permisos.map(permiso => (
                        <option key={permiso.name} value={permiso.name}>{permiso.name}</option>
                    ))}
                </select>
            </div>
            <div className="input-control input-control--buttons">
                <button type="submit" className="btn-save" >Guardar</button>
                <a href="/roles" className="btn-create">cancelar</a>
            </div>
        </form>
    )
}