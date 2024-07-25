import {BrowserRouter, Routes, Route} from 'react-router-dom'
import { RoleListPage } from './pages/RoleListPage'
import { RoleFormPage } from './pages/RoleFormPage'

function App(){
  return(
    <BrowserRouter>
      <Routes>

        <Route path="/roles" element={<RoleListPage/>}/>
        <Route path="/roles-create" element={<RoleFormPage/>}/>

      </Routes>
    </BrowserRouter>
  )
}
export default App