<template>
<v-container>
  <v-tabs v-model="tab_selected">
    <v-tab>Projects</v-tab>
    <v-tab>Projects By Categories</v-tab>
  </v-tabs>

  <div v-if="tab_selected==0">
  
    <v-row>
      <v-col>
        <v-btn text small @click="openDialog=true">
          <v-icon>mdi-plus</v-icon>
          Add new Project
        </v-btn>
              <add-project-dialog 
              :categories="categories"
              :users="users"
              :open="openDialog" 
              @closed="openDialog=false"
              @saved="refreshProjects"/>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="3">
        <h5>Filters</h5>
        <div class="d-flex justify-space-between">
        <v-select class="mr-4"
            v-model="category_selected"
            :items="categories"
            label="Category"
            @change="refreshProjects"
          ></v-select>
          <v-select
            v-model="assignee_selected"
            :items="users"
            label="Assignee"
            item-text="nickname"
            item-value="user_id"
            @change="refreshProjects"
          ></v-select>
        </div>
      </v-col>
    </v-row>
    <ProjectTable :projects="projects" @updated="refreshProjects" />
  </div>
  <div v-else-if="tab_selected==1">
      <v-treeview :items="projects_by_categories"></v-treeview>
  </div>
</v-container>
</template>

<script>
  import ProjectTable from '../components/ProjectTable'
  import AddProjectDialog from '../components/AddProjectDialog'

  export default {
    name: 'Home',

    data() {
      return {
        tab_selected: 0,
        openDialog: false,
        assignee_selected: "",
        category_selected: "",
        projects: [],
        categories: ["All"],
        projects_by_categories: [],
        users: [{nickname: "All"}]
      }
    },

    components: {
      ProjectTable,
      AddProjectDialog
    },

    methods: {
      refreshProjects() {
        this.openDialog=false
        let query_path = ""
        if (this.category_selected && this.category_selected !== "All") {
          query_path += `category=${encodeURIComponent(this.category_selected)}`
        }
        if (this.assignee_selected && this.assignee_selected !== "All") {
          query_path += `&assigned_to=${encodeURIComponent(this.assignee_selected)}`
        }
        this.fetchProjects(query_path)
      },
      fetchProjects(query_path="") {
        return fetch(`http://localhost:3000/projects/?${query_path}`)
          .then(res => {
            return res.json()
          })
          .then(projects => {
            this.projects = projects
            return projects
          })
      },
      initCategories() {
        return this.fetchProjects()
          .then(projects => {
            let cat = projects.reduce((t, p) => {
              if (!t.includes(p.category)) t.push(p.category)
              return t
            }, [])
            this.categories = [...this.categories, ...cat]

            this.projects_by_categories = cat.map(c => {
              return {
                name: c, 
                children: projects
                  .filter(p => p.category==c)
                  .map(p => {
                    return {name: `${p.title} (Assigned to ${p.nickname})`}
                  })}
            })
            
            
            

          })
      },
      initUsers() {
        fetch("http://localhost:3000/users")
          .then(res => {
            return res.json()
          })
          .then(users => {
            this.users = [...this.users, ...users]
          })
      }
    },

    created() {
      this.initCategories()
      this.initUsers()
    }
  }
</script>
