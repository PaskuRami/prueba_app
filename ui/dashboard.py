#The admin dashboard allows for managing users, roles, 
# and displaying role-specific content. This is the CRUD of application.
import streamlit as st
from auth.auth_manager import AuthManager
from auth.hash_utils import hash_password
from auth.jwt_utils import decode_token

#We initialize the authentication manager
auth_manager = AuthManager()

def admin_dashboard():
    """
    Adminitrator dashboard to manage users and roles.
    Provides basic CRUD for users and roles.
    """
    st.title("Administration Panel")
    #Check if the user has an active session
    if "auth_token" not in st.session_state:
        st.warning("Please log in first.")
        st.stop()
    #Decode the token to get the user information
    token_data = decode_token(st.session_state["auth_token"])
    if not token_data or token_data.get("role") != "admin":
        st.error("You do not have permission to access this page.")
        st.stop()
    
    #Tabs to separate user and role management
    tab1, tab2 = st.tabs(["User Management", "Role management"])
    
    #Gestion de Usuarios
    with tab1:
        st.header("User management")
        #Formulario para agregar un nuevo usuario
        st.subheader("Add user")
        new_username = st.text_input("Username", key="new_user_username")
        new_password = st.text_input("Password", type="password", key="new_user_password")
        roles = auth_manager.db.fetchall("SELECT role_name FROM roles")
        new_role = st.selectbox("Role", [r[0] for r in roles], key="new_user_role")
        if st.button("Add user", key="add_user_button"):
            if new_username and new_password and new_role:
                print(f"user: {new_username}, pass: {new_password}, rol: {new_role}")
                try:
                    print(f"valor:")
                    success = auth_manager.register_user(new_username,new_password,new_role)
                    print(f"{success}")
                except KeyError as e:
                    print(f"Error nuevo usuario, {e}")
                if success:
                    st.success(f"User '{new_username}' created succesfully.")
                    st.session_state["auth_token"] = st.session_state["auth_token"]  #keep the token
                    st.rerun()
                else:
                    st.error("All fields are required.")
            
        #Show list of users with option to delete
        st.subheader("Registered Users")
        users = auth_manager.db.fetchall("SELECT id, username, role FROM users")
        for user_id, username, role in users:
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{username}** ({role})")
            if col2.button("Eliminate", key=f"delete_user_button_{user_id}"):
                auth_manager.db.execute("DELETE FROM users WHERE id = ?", (user_id,))
                st.session_state["auth_token"] = st.session_state["auth_token"] #Keep the token
                st.rerun()
            
            #Role Management
    with tab2:
        st.header("Role Management")
        #Formulario para agregar un nuevo rol
        st.subheader("Add Role")
        new_role_name = st.text_input("Role Name", key="new_role_name")
        if st.button("Add Role", key="add_role_button"):
            if new_role_name:
                success = auth_manager.create_role(new_role_name)
                if success:
                    st.success(f"Role '{new_role_name}' Create succesfully.")
                    st.session_state["auth_token"] = st.session_state["auth_token"] #Keep the token
                    st.rerun()
                else:
                    st.error(f"Role '{new_role_name}' already exists.")
            else:
                st.error("The role name is required.")
        #Mostrar lista de roles con opcion para eliminar
        st.subheader("Existing Roles")
        roles = auth_manager.db.fetchall("SELECT id, role_name FROM roles")
        for role_id, role_name in roles:
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{role_name}**")
            if col2.button("Eliminate", key=f"delete_role_button_{role_id}"):
                auth_manager.db.execute("DELETE FROM roles WHERE id = ?", (role_id,))
                st.session_state["auth_token"] = st.session_state["auth_token"] #Keep the token
                st.rerun()

        #Main call to execute the function
if __name__ == "__main__":
    admin_dashboard()