<template>
  <v-dialog v-model="dialog" max-width="600" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon=""
        variant="text"
        v-bind="activatorProps"
      >
        <v-badge color="error" :content="$store.category.categories.length">
          <v-icon size="large">mdi-shape</v-icon></v-badge
        >
      </v-btn>
    </template>

    <v-card prepend-icon="mdi-shape" title="Cadastrar uma nova categoria">
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
      this.$store.category.load()
    }
  }
}
</script>
