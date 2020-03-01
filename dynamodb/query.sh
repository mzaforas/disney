aws dynamodb scan \
     --table-name disneyland \
     --filter-expression "entity_id = :id" \
     --expression-attribute-values '{":id":{"S":"P1DA04"}}'