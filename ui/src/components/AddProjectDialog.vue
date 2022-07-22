<template>
  <v-row justify="center">
    <v-dialog
      v-model="open"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h5">New Project</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="title_selected"
                  label="Project Title*"
                  required
                ></v-text-field>

                <v-select class="mr-4"
                    v-model="category_selected"
                    :items="categories.filter(c=>c!=='All')"
                    label="Category"
                ></v-select>
                <v-select
                    v-model="assignee_selected"
                    :items="users.filter(u => u.nickname!=='All')"
                    label="Assignee"
                    item-text="nickname"
                    item-value="user_id"
                ></v-select>

              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="closeDialog"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="save"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>

export default{
    name: "AddProjectDialog",
    props: ["open", "categories", "users"],
    data() {
        return {
            title_selected: "",
            category_selected: "",
            assignee_selected: ""
        }
    },
    methods: {
        closeDialog() {
            this.$emit("closed")
        },

        async save() {
            if (this.title_selected && this.category_selected && this.assignee_selected) {
                await fetch("http://localhost:3000/projects",{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        title: this.title_selected,
                        category: this.category_selected,
                        assigned_to: this.assignee_selected
                    })
                })
                this.$emit("saved")
            }
        }
    }
}
</script>
