<template>
  <v-dialog
    v-model="dialog"
    max-width="600"
    transition="slide-y-transition"
    persistent
  >
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-shape"
        variant="text"
        v-bind="activatorProps"
      />
    </template>

    <v-card prepend-icon="mdi-bank" title="Cadastrar um novo banco">
      <v-card-text class="py-5">
        <CategoryForm ref="bankForm" @finished="close" @cancel="close" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import CategoryForm from '@/components/forms/CategoryForm.vue'

export default {
  components: {
    CategoryForm
  },
  data: () => ({
    dialog: false
  }),
  methods: {
    close() {
      this.dialog = false
    }
  }
}
</script>
