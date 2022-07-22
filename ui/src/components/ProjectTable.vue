<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="projects"
          :items-per-page="15"
          class="elevation-1"
        >
          <template v-slot:item.delete="{ item }">
            <v-icon @click="deleteItem(item)">
              mdi-delete
            </v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'ProjectTable',
    props: ['projects'],
    data() {
      return {
        headers: [
          {
            text: "Project",
            value: "project_id"
          },
          {
            text: "Title",
            value: "title"
          }, 
          {
            text: "Category",
            value: "category"
          },
          {
            text: "Created At",
            value: "created_timestamp"
          },
          {
            text: "Last Update",
            value: "updated_timestamp"
          },
          {
            text: "Assignee",
            value: "nickname"
          },
          {
            text: "Action",
            value: "delete",
            sortable: false
          }
          
        ]
      }
    },
    methods: {
      deleteItem(item) {
        if (confirm(`Deleting project ${item.title}. Are you sure?`)) {
          fetch(`http://localhost:3000/projects/${item.project_id}`, {
            method:'DELETE'
          })
          .then(() => {
            this.$emit('updated')
          })
        }
      }
    }
  }
</script>
