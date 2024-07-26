import {BrowserRouter, Routes, Route} from 'react-router-dom'
import { RoleListPage } from './pages/RoleListPage'
import { RoleFormPage } from './pages/RoleFormPage'
import  RoleEditPage  from './pages/RoleEditPage'

function App(){
  return(
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<RoleListPage/>}/>
        <Route path="/roles" element={<RoleListPage/>}/>
        <Route path="/roles-create" element={<RoleFormPage/>}/>
        <Route path="/roles-edit/:id" element={<RoleEditPage/>}/>
       
      </Routes>
    </BrowserRouter>
   
    
  )
}
export default App