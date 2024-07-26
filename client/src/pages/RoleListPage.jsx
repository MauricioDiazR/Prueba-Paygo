import { useEffect, useState } from "react"
import RoleList from "../components/rolelist"
import ima from "../../public/Noesmucho.jpg"
export function RoleListPage(){

    const [roles, setRoles] = useState([])

    useEffect(() => {
        const getRoles = async () => {
            const response = await fetch('http://127.0.0.1:8000/roles/')
            const data = await response.json()
            setRoles(data)
        }
        getRoles()
    }, [])

    return(
        <div className="role-list-page">
            <header className="header">
                <h1>RoleL List page</h1>
                <a href="/roles-create" className="btn-go-to-create">Crear nuevo rol</a>
            </header>
            <RoleList roles={roles}/>
            <img src={ima}/>
        </div>
    )
}
